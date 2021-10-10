<template>
    <div class="lesson">
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
            <div v-if="$store.getters.getStaff" @click="showModal" class="lesson_button">
                <div class="nbtn">
                    <div class="btn">Отметить</div>
                </div>
            </div>
        </div>
        <div class="more_time">
            <div class="date">
                 Цена: {{lesson.price}} &nbsp;
            </div>
            <div class="date">
                 Длительность: {{lesson.duration}} &nbsp;
            </div>
            <div class="time">
                {{lesson.time.slice(0, -3) }} &nbsp;
            </div>
            <div class="date">
                 {{lesson.date}}
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