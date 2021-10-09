<template>
    <div class="modal_window">
        <div class="modal_wrapper">
            <div>Занятие </div><p>{{this.id}}</p>
            <slot></slot>
        </div>
        <div @click="close" class="modal_back"></div>
    </div>
</template>

<script>
export default {
    props:{
        someInfo:{
            type: Array,
            required: false
        },
        id: {
          type: Number,
          default: 1
        }
    },
    methods:{
        close(){
            this.$emit('showModal')
        },
    }
}
</script>
