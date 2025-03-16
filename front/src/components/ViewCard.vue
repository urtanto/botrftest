<template>
  <div
      class="flex flex-col items-center justify-center min-h-screen px-4 py-8 text-white bg-gradient-to-b from-purple-600 to-blue-700">
    <p>test</p>
    <div class="mb-6 text-center">
      <h1 class="font-bold text-white">Username: {{ username }}</h1>
      <h1 class="font-bold text-white">First name: {{ first_name }}</h1>
      <h1 class="font-bold text-white">Last name: {{ last_name }}</h1>
      <h1 class="font-bold text-white">осталось:
        {{ days }} дней, {{ hours }} часов, {{ minutes }} минут, {{ seconds }} секунд</h1>
    </div>
  </div>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref, onMounted} from "vue";

const route = useRoute()
const userUuid = route.params.uuid

const response = await fetch(`https://thesortage.space/api/user/${userUuid}`, {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
})

const responseData = await response.json()
const username = ref(responseData.username)
const first_name = ref(responseData.first_name)
const last_name = ref(responseData.last_name)
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)

// const intervalId = setInterval(() => {
//   const now = new Date();
//   let birthday = new Date(responseData.birth_date);
//
//   birthday.setFullYear(now.getFullYear());
//
//   if (birthday < now) {
//     birthday.setFullYear(now.getFullYear() + 1);
//   }
//
//   const diff = birthday.getTime() - now.getTime();
//
//   if (diff <= 0) {
//     days.value = hours.value = minutes.value = seconds.value = 0;
//     clearInterval(intervalId);
//   } else {
//     days.value = Math.floor(diff / (1000 * 60 * 60 * 24));
//     hours.value = Math.floor((diff / (1000 * 60 * 60)) % 24);
//     minutes.value = Math.floor((diff / (1000 * 60)) % 60);
//     seconds.value = Math.floor((diff / 1000) % 60);
//   }
// }, 1000);

onMounted(() => {
  window.Telegram.WebApp.ready()

  const userData = window.Telegram.WebApp.initDataUnsafe.user
  data.tg_id = userData.id
})
</script>