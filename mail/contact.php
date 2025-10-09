<?php
if(empty($_POST['name']) || empty($_POST['subject']) || empty($_POST['message']) || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
  http_response_code(500);
  exit();
}

$name = strip_tags(htmlspecialchars($_POST['name']));
$email = strip_tags(htmlspecialchars($_POST['email']));
$m_subject = strip_tags(htmlspecialchars($_POST['subject']));
$message = strip_tags(htmlspecialchars($_POST['message']));

$to = "info@turkana-prep.ac.ke"; // Turkana Preparatory School email
$subject = "$m_subject:  $name";
$body = "New inquiry from Turkana Preparatory School website:\n\nName: $name\nEmail: $email\nSubject: $m_subject\n\nMessage:\n$message\n\n---\nThis message was sent from the school website contact form.";
$header = "From: $email";
$header .= "Reply-To: $email";	

if(!mail($to, $subject, $body, $header))
  http_response_code(500);
?>
