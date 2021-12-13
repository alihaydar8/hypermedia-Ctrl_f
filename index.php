<?php
    // $command = escapeshellcmd('python python/index.py');
    // $output = shell_exec($command);
    // echo $output;
    require_once "php/config.php";
?>


<!-- CSS only -->
<head>
 <link href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" rel="stylesheet">
   <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="css/index.css" />
</head>

<body>
  <div class="search-container">
    <input type="text" name="search" placeholder="Search..." class="search-input">
    <a href="#" class="search-btn">
      <i class="fas fa-search"></i>      
    </a>
  </div>
  <h4> vdfvdfvdfv </h4>
  <?php
  echo "hi";
    global $Connect;
      $req_competences = "SELECT * 
              FROM cr_f" ;
              echo "hii";	
              $result_competences = $Connect->query($req_competences);	
              echo "Fcf";
              while ($competence = $result_competences->fetch_assoc() )
              {
                $nom=$competence['nom'];
              
              echo $nom;
            }
    ?>
</body>