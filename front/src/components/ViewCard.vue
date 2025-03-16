<template>
  <div
      class="flex flex-col items-center justify-center min-h-screen px-4 py-8 bg-gradient-to-b from-purple-600 to-blue-700 text-white">
    <div class="text-2xl">
      Карточка пользователя <span class="text-2xl font-bold text-orange-600">{{ username }}</span>
    </div>

    <table class="mb-4">
      <tbody>
      <tr>
        <td class="py-2 text-left">First name:</td>
        <td class="px-4 py-2 text-left font-bold">{{ first_name }}</td>
      </tr>
      <tr>
        <td class="py-2 text-left">Last name:</td>
        <td class="px-4 py-2 text-left font-bold">{{ last_name }}</td>
      </tr>
      </tbody>
    </table>

    <div class="mb-2 text-sm">
      Осталось до дня рождения:
    </div>

    <div class="mb-8 text-xl font-thin">
      <span class="font-bold">{{ days }}</span>
      дней
      <span class="font-bold">{{ hours }}</span>
      часов
      <span class="font-bold">{{ minutes }}</span>
      минут
      <span class="font-bold">{{ seconds }}</span>
      секунд
    </div>

    <button
        v-if="mycard()"
        @click="share"
        class="px-6 py-3 bg-white text-purple-600 font-bold rounded shadow hover:bg-purple-100 transition mb-4">
      Поделиться
    </button>

    <button
        v-if="!mycard()"
        @click="create_my"
        class="px-6 py-3 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-bold rounded shadow hover:from-purple-600 hover:to-blue-600 transition">
      Сгенерировать свою карточку
    </button>
  </div>
</template>


<script setup>
import {useRoute} from 'vue-router'
import {ref, onMounted} from "vue";
import router from "@/router/index.js";

const route = useRoute()
const userUuid = route.params.uuid

let tg_id = null
let card_tg_id = null
const username = ref('')
const first_name = ref('')
const last_name = ref('')
let birth_date
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)

onMounted(async () => {
  const response = await fetch(`https://thesortage.space/api/user/${userUuid}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
  })

  const responseData = await response.json()
  card_tg_id = responseData.tg_id
  username.value = responseData.username
  first_name.value = responseData.first_name
  last_name.value = responseData.last_name
  birth_date = responseData.birth_date

  if (window.Telegram.WebApp) {
    window.Telegram.WebApp.ready()

    const userData = window.Telegram.WebApp.initDataUnsafe.user
    tg_id = userData?.id ?? null
  }
})

setInterval(() => {
  const now = new Date();
  let birthday = new Date(birth_date);

  birthday.setFullYear(now.getFullYear());
  birthday.setDate(birthday.getDate() - 1);

  let diff = birthday.getTime() - now.getTime();

  if (diff <= 0) {
    birthday.setFullYear(now.getFullYear() + 1);
    diff = birthday.getTime() - now.getTime();
  }

  days.value = Math.floor(diff / (1000 * 60 * 60 * 24));
  hours.value = Math.floor((diff / (1000 * 60 * 60)) % 24);
  minutes.value = Math.floor((diff / (1000 * 60)) % 60);
  seconds.value = Math.floor((diff / 1000) % 60);
}, 1000);

const share = () => {
  if (navigator.share) {
    const link = `https://t.me/robita_task_bot/TestBirtdayMiniApp?startapp=${userUuid}`
    navigator.share({
      title: 'Моя карточка',
      url: link,
    })
  } else {
    alert('Ваш браузер не поддерживает функцию "Поделиться"')
  }
}

function create_my() {
  router.push('/')
}

function mycard() {
  return tg_id === card_tg_id
}
</script>