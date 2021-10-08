<template>
    <div>
        <Nuxt/>
        <Header/>
        <div class="back_gib">
            <img src="~/static/images/gib.png" alt="">
        </div>
    </div>
</template>

<script>
import Header from '@/components/main/Header'
export default {
    components:{ Header},
}
</script>