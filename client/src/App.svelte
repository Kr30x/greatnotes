<script>
  import Navbar from './Components/Navbar/Navbar.svelte';
</script>

<style>


  :global(body) { margin: 0; padding: 0;}
  body {
    
    margin: 0;
    padding: 0;
    background-color: #f9f9f9; 
    color: #000000;
    height: auto;
    overflow-x: hidden;
    overflow-y: scroll;
  }


  :global(body)::-webkit-scrollbar {
    width: 0.5rem;
  }

  :global(body)::-webkit-scrollbar-thumb {
    background-color: #3498db;
    border-radius: 6px;
  }

  :global(body)::-webkit-scrollbar-track {
    /* background-color: #f1f1f1; */
  }

  /* Firefox */
  :global(body) {
    scrollbar-width: thin;
    scrollbar-color: #3498db #f1f1f1;
  }

  /* Microsoft Edge and Internet Explorer */
  :global(body) {
    -ms-overflow-style: none;
  }

  :global(body)::-ms-scrollbar-thumb {
    background-color: #3498db;
    border-radius: 6px;
  }

  :global(body)::-ms-scrollbar-track {
    background-color: #f1f1f1;
  }


</style>


<Navbar />
