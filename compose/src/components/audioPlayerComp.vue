<template>
  <div>
    <p>
      {{ defaultMessage }}
    </p>
    <div>
      <audio
        controls
        :src="defaultAudioURL"
        ref="mainAudio"
        @ended="endPlay"
      ></audio>
      <el-button @click="changeAudioAndReload">change audio</el-button>
    </div>
  </div>
</template>

<script>
import { toRefs, h } from "vue";
import { ElNotification } from "element-plus";
import { useStore } from "vuex";

export default {
  name: "audioPlayerComp",
  props: ["defaultMessage", "defaultAudioURL"],
  setup(props) {
    // TODO: 思考为什么这两个的proxy是readonly的属性？
    let { defaultMessage, defaultAudioURL } = toRefs(props);

    const store = useStore();

    // get new audio url from localStorage
    const getAudioURL = () => {
      let audioInfo = store.getters.audioInfo;
      return audioInfo.audioURL;
    };

    // A function which will be used when audio play is end
    const endPlay = () => {
      ElNotification({
        title: "感谢聆听",
        message: h("i", { style: "color: teal" }, "这里是歌词"),
      });
    };

    return {
      // eslint-disable-next-line
      defaultMessage,
      // eslint-disable-next-line
      defaultAudioURL,
      endPlay,
      getAudioURL,
    };
  },
  methods: {
    changeAudioAndReload() {
      // eslint-disable-next-line
      this.$refs.mainAudio.src = this.getAudioURL();
      // TODO: need to fix this in setup
      console.log("Reload audio in url: " + this.$refs.mainAudio.src);
      this.$refs.mainAudio.play();
    },
  },
};
</script>

<style scoped></style>
