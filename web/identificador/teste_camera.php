<!DOCTYPE html>
<html>
    <head>
    	<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
    
        <title>getUserMedia</title>
    </head>
    <body>
        <header>
            <h1>getUserMedia</h1>
        </header>
        <article>
            <video  id="video" width="320" height="200" autoplay></video>
            <section>
                <button id="btnStart">Start video</button>
                <button id="btnStop">Stop video</button>            
                <button id="btnPhoto">Take a photo</button>
            </section>
            
            <canvas id="canvas" width="320" height="240"></canvas>
        </article>
        
        <script type="text/javascript">
        	var img;
	        window.onload = function() {
	
	            //Compatibility
	            navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
	
	            var canvas = document.getElementById("canvas"),
	                context = canvas.getContext("2d"),
	                video = document.getElementById("video"),
	                btnStart = document.getElementById("btnStart"),
	                btnStop = document.getElementById("btnStop"),
	                btnPhoto = document.getElementById("btnPhoto"),
	                videoObj = {
	                    video: true,
	                    audio: false
	                };
	
	            btnStart.addEventListener("click", function() {
	                var localMediaStream;
	
	                if (navigator.getUserMedia) {
	                    navigator.getUserMedia(videoObj, function(stream) {              
	                        video.src = (navigator.webkitGetUserMedia) ? window.webkitURL.createObjectURL(stream) : stream;
	                        localMediaStream = stream;
	                        
	                    }, function(error) {
	                        console.error("Video capture error: ", error.code);

	                    });
	                	
	                    btnStop.addEventListener("click", function() {
	                        localMediaStream.stop();
	                        
	                    });
	
	                    btnPhoto.addEventListener("click", function() {
	                        context.drawImage(video, 0, 0, 320, 240);

	                        img = canvas.toDataURL("image/png");
	                        formulario.img64.value = img;

							
	                    });

	                    
	                }
	            });
	        };
	       

        </script>
        
        
        <form id="formulario" enctype="multipart/form-data" action="enviar.php" method="POST" id="youform" name="youform">
            <input type="hidden" name="MAX_FILE_SIZE" value="30000" />
            Base64 do canvas: <input name="img64" id="img64" type="hidden" />
            
            <input type="submit" value="Enviar arquivo" onsubmit="document.getElementById('img64').value = img" />
        </form>
        
    </body>
</html>