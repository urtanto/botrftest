<template>
  <div class="flex flex-col items-center justify-center min-h-screen px-4 py-8 bg-gradient-to-b from-purple-600 to-blue-700 text-white">
    <!-- Таблица для выравнивания данных пользователя, без видимых границ -->
    <table class="mb-4">
      <tbody>
        <tr>
          <td class="px-4 py-2 text-left font-bold">Username:</td>
          <td class="px-4 py-2 text-left">{{ username }}</td>
        </tr>
        <tr>
          <td class="px-4 py-2 text-left font-bold">First name:</td>
          <td class="px-4 py-2 text-left">{{ first_name }}</td>
        </tr>
        <tr>
          <td class="px-4 py-2 text-left font-bold">Last name:</td>
          <td class="px-4 py-2 text-left">{{ last_name }}</td>
        </tr>
      </tbody>
    </table>

    <div class="mb-2 text-sm">
      Осталось до дня рождения:
    </div>

    <div class="mb-8 text-xl font-bold">
      {{ days }} дней {{ hours }} часов {{ minutes }} минут {{ seconds }} секунд
    </div>

    <button
      @click="share"
      class="px-6 py-3 bg-white text-purple-600 font-bold rounded shadow hover:bg-purple-100 transition">
      Поделиться
    </button>
  </div>
</template>


<script setup>
import {useRoute} from 'vue-router'
import {ref, onMounted} from "vue";

const route = useRoute()
const userUuid = route.params.uuid

let tg_id = null
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
  } else {
    days.value = Math.floor(diff / (1000 * 60 * 60 * 24));
    hours.value = Math.floor((diff / (1000 * 60 * 60)) % 24);
    minutes.value = Math.floor((diff / (1000 * 60)) % 60);
    seconds.value = Math.floor((diff / 1000) % 60);
  }
}, 1000);

const share = () => {
  if (navigator.share) {
    navigator.share({
      title: 'Моя карточка',
      url: window.location.href,
    })
    .then(() => console.log('Share successful'))
    .catch((error) => console.error('Error sharing', error))
  } else {
    alert('Ваш браузер не поддерживает функцию "Поделиться"')
  }
}
</script>