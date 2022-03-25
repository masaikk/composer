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

export default {
  name: "audioPlayerComp",
  props: ["defaultMessage", "defaultAudioURL"],
  setup(props) {
    // TODO: 思考为什么这两个的proxy是readonly的属性？
    let { defaultMessage, defaultAudioURL } = toRefs(props);

    // get new audio url from localStorage
    const getAudioURL = () => {
      let randomNumber = Math.floor(1 + 4 * Math.random());
      // TODO: must fix this
      // 获取真实的数据
      return `http://119.23.182.180/azur/t${randomNumber}.mp3`;
    };

    // A function which will be used when play is end
    const endPlay = () => {
      ElNotification({
        title: "Title",
        message: h("i", { style: "color: teal" }, "This is a reminder"),
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
