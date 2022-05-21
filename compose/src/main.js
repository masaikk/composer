import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import { createI18n } from "vue-i18n";
import { messages } from "@/lang";

const i18n = createI18n({
  locale: "zh",
  fallbackLocale: "en",
  legacy: false,
  messages,
});

const app = createApp(App);
app.use(ElementPlus);
app.use(store);
app.use(i18n);
app.use(router);

app.mount("#app");
