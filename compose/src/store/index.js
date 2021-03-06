import { createStore } from "vuex";

export default createStore({
  state: {
    currentAudioURL: "http://119.23.182.180/azur/t1.mp3",
    currentLyrics: "This is a sentence",
    isUsedFlag: false,
    isFlesh: false,
    currentUid: 1,
    currentName: "用户",
    currentLocale: "zh",
  },
  getters: {
    audioInfo(state) {
      return {
        audioURL: state.currentAudioURL,
        usedFlag: state.isUsedFlag,
        fleshFlag: state.isFlesh,
        lyrics: state.currentLyrics,
      };
    },
    // 返回一个返回歌词的函数用于调用
    getLyrics(state) {
      return function () {
        return state.currentLyrics;
      };
    },
    getCurrentLocale(state) {
      return function () {
        return state.currentLocale;
      };
    },
    getUid(state) {
      return function () {
        return state.currentUid;
      };
    },
    getName(state) {
      return function () {
        return state.currentName;
      };
    },
  },
  mutations: {
    setAudioURLAndFlag(state, info) {
      state.currentAudioURL = info.audioURL;
      state.usedFlag = false;
    },
    setCurrentLocale(state, locale) {
      state.currentLocale = locale;
    },
    setFlagFalse(state) {
      state.isUsedFlag = false;
    },
    setFlagTrue(state) {
      state.isUsedFlag = true;
    },
    setLyrics(state, lyrics) {
      state.currentLyrics = lyrics;
    },
    setUid(state, uid) {
      state.currentUid = parseInt(uid);
    },
    setName(state, name) {
      state.currentName = name;
    },
  },
  actions: {},
  modules: {},
});
