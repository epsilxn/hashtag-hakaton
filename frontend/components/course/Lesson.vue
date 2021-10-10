<template>
    <div class="lesson">
        <h1>{{lesson.price}}</h1>
        <div class="lesson_count">
            {{idx}}
        </div>
        <div class="lesson_more">
            <div class="more_name">
                {{lesson.name}}
            </div>
            <div class="more_info">
                {{lesson.information}}
            </div>
            <div @click="showModal" class="lesson_button">
                <div class="nbtn">
                    <div class="btn">Отметить</div>
                </div>
            </div>
        </div>
        <div class="more_time">
            <div class="time">
                {{lesson.time.slice(0, -3) }} &nbsp;
            </div>
            <div class="date">
                 {{lesson.date}} &nbsp;
            </div>
            <div class="duration">
                {{lesson.duration}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        lesson:{
            type: Object,
            required: true
        },
        idx:{
            type: Number,
            default: 1
        }
    },
    methods:{
        showModal(){
            this.$emit('showModal')
        }
    }
}
</script>
