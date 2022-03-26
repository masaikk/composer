import { createStore } from "vuex";

export default createStore({
  state: {
    currentAudioURL: "http://119.23.182.180/azur/t1.mp3",
    currentLyrics: "This is a sentence",
    isUsedFlag: false,
    isFlesh: false,
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
  },
  mutations: {
    setAudioURLAndFlag(state, info) {
      // console.log(state);
      // console.log(info);
      state.currentAudioURL = info.audioURL;
      state.usedFlag = false;
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
  },
  actions: {},
  modules: {},
});
