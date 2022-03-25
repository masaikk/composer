import { createStore } from "vuex";

export default createStore({
  state: {
    currentAudioURL: "http://119.23.182.180/azur/t1.mp3",
    isUsedFlag: false,
  },
  getters: {
    audioInfo(state) {
      return {
        audioURL: state.currentAudioURL,
        usedFlag: state.isUsedFlag,
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
  },
  actions: {},
  modules: {},
});
