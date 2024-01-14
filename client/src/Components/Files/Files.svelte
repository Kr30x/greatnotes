<script>
    
    import DirectoryCard from '../DirectoryCard/DirectoryCard.svelte';
    import FileCard from '../FileCard/FileCard.svelte';
    import Files from './Files.svelte';
    let rand = ['Loading...'];

    export let directory = '';
    export let IndentDepth = 0;

    function get_directory(dir) {
        console.log("./get_folder/" + dir);
        fetch("./get_folder/" + dir).then(d => d.json()).then(d => (rand = d));
    }

    function is_file(str){
        const fileExtensionRegex = /\.[0-9a-z]+$/i;

        // Check if the string ends with a file extension
        if (fileExtensionRegex.test(str)) {
            return true; // It's a file name
        } else {
            return false; // It's a directory name
        }
    }

    get_directory(directory);
</script>

<div style='margin-left:{IndentDepth * 20}px'>
    {#each rand as item}
        {#if item === 'Loading...' || is_file(item)}
            <FileCard FileName = {item}/>
        {:else}
            <DirectoryCard DirectoryName = {item} DirectoryParentPath = {directory}/>
        {/if}
    {/each}
</div>
<style>
    
</style>


