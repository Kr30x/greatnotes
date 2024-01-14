<script>
    export let FileName = 'undefined file name';

    import { active_file } from '../../stores/store.js'

    let is_open = 'closed';

    function open_file(){
        if (is_open === 'closed'){
            is_open = 'open';
            $active_file = FileName;
            console.log($active_file);
        }
        else{
            is_open = 'closed';
            $active_file = '';
        }
    }

</script>

<div on:click = {open_file} class = {is_open}>
    <p>{FileName}</p>
</div>


<style>
    div {
        width: auto;
        cursor: pointer;
        background-color: #f5f5f5;
        border-radius: 16px;
        padding: 4px;
        transition: all 0.3s ease-in-out;
        margin-bottom: 7px;
    }

    div p{
        margin: 0px;
        margin-left: 5px;
    }

    div:hover{
        background-color: #c4c4c4;
    }

    .open{
        background-color: #c4c4c4;
    }
</style>