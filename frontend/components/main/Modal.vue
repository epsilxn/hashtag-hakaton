<template>
    <div class="modal_window">
        <div class="modal_wrapper">

        </div>
        <div @click="close" class="modal_back"></div>
    </div>
</template>

<script>
export default {
    props:{
        someInfo:{
            type: Array,
            required: true
        }
    },
    methods:{
        close(){
            this.$emit('showModal')
        },
    }
}
</script>
