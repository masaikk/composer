import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/compose",
    name: "compose",
    component: () => import("../views/composeMainPage.vue"),
    children: [
      {
        path: "about",
        component: () => import("../views/AboutView.vue"),
      },
      {
        path: "main",
        name: "main",
        component: () =>
          import(
            /* webpackChunkName: "mainComposer" */ "../views/composeMain.vue"
          ),
      },
      {
        path: "history",
        name: "history",
        component: () => import("../views/melodyComposeHisView.vue"),
      },
      {
        path: "myself",
        name: "myself",
        component: () => import("../views/AboutMyself.vue"),
      },
      {
        path: "comment",
        name: "comment",
        component: () => import("../views/commentView.vue"),
      },
    ],
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/userLogin.vue"),
  },
  {
    path: "/404",
    name: "404Page",
    component: () => import("../views/my404Page.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
