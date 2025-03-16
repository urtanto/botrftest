<script setup>
import {useRoute} from 'vue-router'

const route = useRoute()
const userUuid = route.params.uuid
</script>

<template>
  <div>
    <h1>Страница пользователя</h1>
    <p>UUID пользователя: {{ userUuid }}</p>
  </div>
</template>

