<?php
function http_get_contents($url)
{
  $ch = curl_init();
  
  curl_setopt($ch, CURLOPT_TIMEOUT, 1);
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
  
  if(FALSE === ($retval = curl_exec($ch))) {
    error_log(curl_error($ch));
  } else {
    return $retval;
  }
}

function prettyPrint( $json )
{
    $result = '';
    $level = 0;
    $in_quotes = false;
    $in_escape = false;
    $ends_line_level = NULL;
    $json_length = strlen( $json );

    for( $i = 0; $i < $json_length; $i++ ) {
        $char = $json[$i];
        $new_line_level = NULL;
        $post = "";
        if( $ends_line_level !== NULL ) {
            $new_line_level = $ends_line_level;
            $ends_line_level = NULL;
        }
        if ( $in_escape ) {
            $in_escape = false;
        } else if( $char === '"' ) {
            $in_quotes = !$in_quotes;
        } else if( ! $in_quotes ) {
            switch( $char ) {
                case '}': case ']':
                    $level--;
                    $ends_line_level = NULL;
                    $new_line_level = $level;
                    break;

                case '{': case '[':
                    $level++;
                case ',':
                    $ends_line_level = $level;
                    break;

                case ':':
                    $post = " ";
                    break;

                case " ": case "\t": case "\n": case "\r":
                    $char = "";
                    $ends_line_level = $new_line_level;
                    $new_line_level = NULL;
                    break;
            }
        } else if ( $char === '\\' ) {
            $in_escape = true;
        }
        if( $new_line_level !== NULL ) {
            $result .= "\n".str_repeat( "\t", $new_line_level );
        }
        $result .= $char.$post;
    }

    return $result;
}

	$responsex = http_get_contents("http://127.0.0.1:5000/mine_block");
	echo $responsex;
    
    $r2x = json_decode($responsex, true);
	
	prettyPrint( $responsex ) === prettyPrint( prettyPrint( $responsex ) )
	/*
	$response2 = http_get_contents("http://127.0.0.1:5000/mine_block");
	echo $response2;
	*/
	
?>
<!DOCTYPE html>
<html>
<head>
    <title>something</title>
    <style>
        th, td, p, input {
            font:14px Verdana;
        }
        table, th, td 
        {
            border: solid 1px #DDD;
            border-collapse: collapse;
            padding: 2px 3px;
            text-align: center;
        }
        th {
            font-weight:bold;
        }
    </style>
</head>
<body>
   // <input type="button" onclick="CreateTableFromJSON()" value="show"></input>
   // <p id="showData"></p>
<div id="terminal_banner"> </div>
<div align="center" >
<a href="/UI/UI.php" class="button1">Get another Block</a> <!-- &nbsp;  &nbsp; -->
<br>
</div>
</body>
</html>