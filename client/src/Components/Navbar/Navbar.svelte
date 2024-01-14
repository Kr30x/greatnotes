<script>
    import Files from '../Files/Files.svelte'
</script>
  
<nav>
    <h1>Конспекты</h1>
    <Files directory={'client/src/notes'}/>
</nav>  

<style>
    nav {
        height: 100%;
        position: fixed;
        min-height: 100vh;
        width: 200px;
        background-color: #e8e8e8;
        box-shadow: 0px 0px 10px 2px #cecece;
        padding: 10px;
    }
    h1 {
        text-align: center;
        font-size: larger;
    }
</style>


