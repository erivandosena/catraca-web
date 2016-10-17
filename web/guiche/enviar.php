<!DOCTYPE html>
<html>
    <head>
        <title>TODO supply a title</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <?php

        
            
            define('UPLOAD_DIR', 'fotos/');
            $img = $_POST['img64'];
            $img = str_replace('data:image/png;base64,', '', $img);
            $img = str_replace(' ', '+', $img);
            $data = base64_decode($img);
            $file = UPLOAD_DIR .$_POST['id_usuario']. '.png';
            $success = file_put_contents($file, $data);
            print $success ? "Foto salva com sucesso!" : 'Erro ao tentar salvar arquivo.';
            echo '<meta http-equiv="refresh" content="2; url=.\?pagina=cartao&selecionado=' . $_POST['id_usuario'] . '">';
        
            
         ?>
    </body>
</html>

