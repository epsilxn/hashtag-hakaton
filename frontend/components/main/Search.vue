<template>
    <div class="search_wrapper">
        <input @input="onInput" 
            placeholder="Найти курс"
            type="text"/>
        <button>
            <span class="material-icons">
                search
            </span>
        </button>
    </div>
</template>

<script>
    export default {
        methods:{
            onInput(event){
                this.$emit('onInput', event.target.value)
            }
        }
    }
</script>

