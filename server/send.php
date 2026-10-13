<?php
// Contact form for smartfinance-nrw.de: receives the request from the page
// and e-mails it to the office from this server, with no third party.
declare(strict_types=1);

const MAIL_TO   = 'info@smartfinance-nrw.de';
const MAIL_FROM = 'info@smartfinance-nrw.de';   // sender shown in the inbox
const ORIGINS   = ['https://www.smartfinance-nrw.de', 'https://smartfinance-nrw.de'];
const MAX_PER_HOUR = 6;                          // per visitor IP

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && in_array($origin, ORIGINS, true)) {
    header('Access-Control-Allow-Origin: ' . $origin);
    header('Vary: Origin');
}
if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') {
    header('Access-Control-Allow-Methods: POST');
    header('Access-Control-Allow-Headers: Content-Type');
    exit;
}
function done(int $code, bool $ok, string $msg = ''): void {
    http_response_code($code);
    echo json_encode(['success' => $ok ? 'true' : 'false', 'message' => $msg]);
    exit;
}
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') done(405, false, 'method');
if ($origin !== '' && !in_array($origin, ORIGINS, true)) done(403, false, 'origin');

$raw = file_get_contents('php://input', false, null, 0, 20000) ?: '';
$in = json_decode($raw, true);
if (!is_array($in)) $in = $_POST;

// bots fill in the hidden field; tell them it worked and drop the message
if (trim((string)($in['_honey'] ?? '')) !== '') done(200, true);

// a few requests per hour and visitor are plenty
$ip = $_SERVER['REMOTE_ADDR'] ?? '0';
$bucket = sys_get_temp_dir() . '/sfc_' . hash('sha256', $ip . date('YmdH'));
$count = (int)@file_get_contents($bucket);
if ($count >= MAX_PER_HOUR) done(429, false, 'rate');
@file_put_contents($bucket, (string)($count + 1));

$clean = static function ($v, int $max): string {
    $v = trim(str_replace(["\r", "\0"], '', (string)$v));
    return mb_substr($v, 0, $max);
};
$name    = $clean($in['name'] ?? '', 120);
$firma   = $clean($in['firma'] ?? '', 160);
$email   = $clean($in['email'] ?? '', 160);
$tel     = $clean($in['tel'] ?? '', 60);
$thema   = $clean($in['thema'] ?? '', 120);
$msg     = $clean($in['nachricht'] ?? '', 5000);
$sprache = $clean($in['sprache'] ?? '', 5);

if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) done(422, false, 'fields');
$oneLine = static fn(string $s): string => str_replace("\n", ' ', $s);

$subject = 'Neue Anfrage über smartfinance-nrw.de – ' . $oneLine($name);
$body = "Neue Anfrage über das Kontaktformular\n"
      . "======================================\n\n"
      . "Name:         " . $oneLine($name) . "\n"
      . "Unternehmen:  " . $oneLine($firma) . "\n"
      . "E-Mail:       " . $email . "\n"
      . "Telefon:      " . $oneLine($tel) . "\n"
      . "Thema:        " . $oneLine($thema) . "\n"
      . "Sprache:      " . $oneLine($sprache) . "\n\n"
      . "Nachricht:\n" . $msg . "\n\n"
      . "--\nGesendet am " . date('d.m.Y H:i') . " über www.smartfinance-nrw.de\n";
$headers = implode("\r\n", [
    'From: ' . mb_encode_mimeheader('Website Smart Finance', 'UTF-8') . ' <' . MAIL_FROM . '>',
    'Reply-To: ' . $email,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
]);
$sent = mail(MAIL_TO, mb_encode_mimeheader($subject, 'UTF-8'), $body, $headers, '-f' . MAIL_FROM);
$sent ? done(200, true) : done(500, false, 'mail');
