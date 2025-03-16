import './assets/tailwind.css'

import {createApp} from 'vue'
import App from './App.vue'
import router from "@/router/index.js";
import { VueTelegramPlugin } from "vue-tg";

const app = createApp(App);
app.use(router)
app.use(VueTelegramPlugin);
app.mount('#app');
