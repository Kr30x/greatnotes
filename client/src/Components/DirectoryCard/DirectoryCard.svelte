<script>
    export let DirectoryName = 'undefined directory name';
    export let DirectoryParentPath = 'undefined parent path';
    export let IndentDepth = 0;
    import Files from "../Files/Files.svelte";

    let is_open = 'closed';

    function open_folder(){
        if (is_open === 'closed'){
            is_open = 'open';
        }
        else{
            is_open = 'closed';
        }
    }
</script>

<div class='folder' on:click={open_folder}>
    <img src='arrow.png' alt='arrow image' class='{is_open}'/>
    <p>{DirectoryName}</p>
</div>

<div>
    {#if is_open === 'open'}
        <Files directory={DirectoryParentPath + '/' + DirectoryName} IndentDepth={IndentDepth + 1}/>
    {/if}
</div>

<style>
    .folder {
        display: flex;
        width: auto;
        cursor: pointer;
        background-color: #f5f5f5;
        border-radius: 16px;
        padding: 8px;
        transition: all 0.3s ease-in-out;
        margin-bottom: 7px;
        /* justify-content: center; */
        align-items: center;
    }

    .folder img{
        height: 10px;
    }

    .open{
        transform: rotate(90deg);
    }

    .folder p{
        margin: 0px;
        margin-left: 5px;
    }

    .folder:hover{
        background-color: #c4c4c4;
    }
</style>