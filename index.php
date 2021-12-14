<?php
// $command = escapeshellcmd('python python/index.py');
// $output = shell_exec($command);
// echo $output;
// require_once "php/config.php";
?>

<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<?php
$bdd = new PDO('mysql:host=127.0.0.1;dbname=hypermedia;charset=utf8', 'hypermedia', 'hypermedia');

if (isset($_GET['search']) and !empty($_GET['search'])) {
  $search = htmlspecialchars($_GET['search']);
  $resultat = $bdd->query('SELECT * FROM cr_f WHERE nom LIKE "%' . $search . '%" ORDER BY occ DESC');
}
?>

<body>
  <figure class="text-center">
    <blockquote class="blockquote">
      <h1>My search Bar</h1>
    </blockquote>
  </figure>
  <div class="d-flex justify-content-center">
    <form class="d-md-flex " method="GET">
      <input class="form-control me-2" name="search" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-success" type="submit">Search</button>
    </form>
  </div>

  <?php
  if ($resultat->rowCount() > 0) { ?>
    <ul class="list-group">
      <?php while ($hay = $resultat->fetch()) { ?>
        <li class="list-group-item"><?php echo "$hay[id]     $hay[nom]  $hay[fichier]  ($hay[occ]) " ?> <a href=<?php echo " $hay[fichier] "?>>Authentification</a> </li>
      <?php } ?>
    </ul>
  <?php } else { ?>
    Aucun résultat pour:
  <?php }
  ?>
</body>