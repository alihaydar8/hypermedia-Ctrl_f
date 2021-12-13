<?php
    // $command = escapeshellcmd('python python/index.py');
    // $output = shell_exec($command);
    // echo $output;
    // require_once "php/config.php";
?>

<?php
 
  $bdd = new PDO('mysql:host=127.0.0.1;dbname=hypermedia;charset=utf8','hypermedia','hypermedia');
 
if(isset($_GET['search']) AND !empty($_GET['search'])) {
   $search = htmlspecialchars($_GET['search']);
   $resultat = $bdd->query('SELECT * FROM cr_f WHERE nom LIKE "%'.$search.'%" ORDER BY occ DESC');
   if($resultat->rowCount() == 0) {
      echo "Databasses vides";
   }
  }
?>
<!-- CSS only -->
<!-- <head>
 <link href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" rel="stylesheet">
   <link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
   <link rel="stylesheet" href="css/index.css" />
</head> -->

<body>
  <div >
    <form method="GET">
    <input type="text" name="search" placeholder="Search..." class="search-input">
    <input type="submit" class="search-btn" />
    </form>
  <?php   
    if($resultat->rowCount() > 0) {?>
      <ul>
        <?php while($hay = $resultat->fetch()) 
          { ?>
            <li><?php echo " $hay[nom]  $hay[fichier]  ($hay[occ]) " ?> <a href= "<?php $hay['fichier'] ?> " >Authentification</a> </li>
          <?php } ?>
      </ul>
    <?php } 
    else { ?>
      Aucun résultat pour: 
    <?php }
  ?>
</body>