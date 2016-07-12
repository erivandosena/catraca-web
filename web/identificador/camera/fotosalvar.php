<?php 

$data = file_get_contents('php://input');

$canvasImg = imagecreatefrompng($data);
$width  = imagesx($canvasImg);
$height = imagesy($canvasImg);

$outImg = imagecreatetruecolor($width, $height);
$color = imagecolorallocatealpha($outImg, 255, 255, 255, 127);
imagefill($outImg, 0, 0, $color);
imagecopy($outImg, $canvasImg, 0, 0, 0, 0, $width, $height);

imagepng($outImg, 'test.png');

?>