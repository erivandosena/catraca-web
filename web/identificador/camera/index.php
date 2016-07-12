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


		                       

		                       var xmlhttp;
		                       xmlhttp=((window.XMLHttpRequest)?new XMLHttpRequest():new ActiveXObject("Microsoft.XMLHTTP"));
		                       xmlhttp.onreadystatechange=function()
		                       {
		                         if (xmlhttp.readyState==4 && xmlhttp.status==200)
		                           {
		                               //do something with the response
		                           }
		                       }
		                       xmlhttp.open("POST","fotosalvar.php",true);
		                       var oldCanvas = canvas.toDataURL("image/png");
		                       var img = new Image();
		                       img.src = oldCanvas;
		                       xmlhttp.setRequestHeader("Content-type", "application/upload")
		                       xmlhttp.send(oldCanvas);
	                        
	                    });

	                    
	                }
	            });
	        };
	       

        </script>
    </body>
</html>