<?php

// check the header for the SECRET KEY
if ( 'POST' != $_SERVER['REQUEST_METHOD'] ) {
	header('Allow: POST');
	header('HTTP/1.1 405 Method Not Allowed');
	header('Content-Type: text/plain');
	exit;
}

$headers = apache_request_headers();
if ( ! array_key_exists('x-api-key', $headers)){
    exit;
}
if ($headers['x-api-key'] != "extravagant-lemur"){
    exit;
}

if (! array_key_exists('title', $_POST)){
    exit;
}
$title = $_POST['title'];

$category = array_key_exists('category', $_POST) ? $_POST['category'] : "Recipies";

if (! array_key_exists('tags', $_POST)){
    exit;
}
$tags = $_POST['tags'];
if (! array_key_exists('body', $_POST)){
    exit;
}
$body = $_POST['body'];

echo $title . " " . $category . " " . $body;