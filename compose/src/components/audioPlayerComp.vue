<template>
  <div>
    <p>
      {{ audioData.audioMessage }}
    </p>
    <div>
      <audio src="" ref="mainAudioNode" @ended="endPlay"></audio>

      <el-button @click="changeAudioAndReload">播放音乐！</el-button>
    </div>
  </div>
</template>

<script>
import { toRefs, h, reactive } from "vue";
import { ElNotification } from "element-plus";
import { useStore } from "vuex";

export default {
  name: "audioPlayerComp",
  props: ["defaultMessage", "defaultAudioURL"],
  setup(props) {
    const { defaultMessage, defaultAudioURL } = toRefs(props);

    let audioData = reactive({
      audioMessage: defaultMessage.value,
      audioURL: defaultAudioURL.value,
    });

    /*    // 获取音乐播放节点
        const mainAudioNode = ref(null);*/

    // 获取VueX
    const store = useStore();

    // get new audio url from localStorage
    const getAudioURL = () => {
      let audioInfo = store.getters.audioInfo;
      return audioInfo.audioURL;
    };

    // A function which will be used when audio play is end
    const endPlay = () => {
      // 从VueX中获取歌词信息用于在消息框中表示
      let lyrics = store.getters.getLyrics();

      ElNotification({
        title: "感谢聆听",
        message: h("i", { style: "color: teal" }, lyrics),
      });
    };

    /*    const changeAudioAndReloadSetup = (audioNode) => {
          let nowAudioURL = getAudioURL();
          console.log(audioNode.value);
          audioNode.value.src = nowAudioURL;
          audioNode.value.play();
          console.log("changeAudioAndReloadSetup " + nowAudioURL);
        };*/

    return {
      audioData,
      endPlay,
      getAudioURL,
    };
  },
  methods: {
    changeAudioAndReload() {
      // eslint-disable-next-line
      this.$refs.mainAudioNode.src = this.getAudioURL();
      // TODO: need to fix this in setup
      console.log(
        "Reload (methods) audio in url: " + this.$refs.mainAudioNode.src
      );
      this.$refs.mainAudioNode.play();
    },
  },
};
</script>

<style scoped></style>
