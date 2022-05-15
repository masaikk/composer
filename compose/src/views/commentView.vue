<template>
  <div>
    <el-container id="comment-header">
      <div>
        <h3>精彩评论</h3>
        <el-button @click="flushCommentsList">刷新评论</el-button>
      </div>
    </el-container>

    <div id="comment-list-holder">
      <el-table :data="commentsList.data" stripe id="comment-data">
        <el-table-column prop="cid" label="序号" />
        <el-table-column prop="uid" label="用户ID" />
        <el-table-column prop="comment" label="评论" />
        <el-table-column prop="time" label="时间" />
      </el-table>
    </div>
    <div id="comment-add-holder">
      <el-input
        placeholder="输入您的评论"
        clearable
        v-model="commentSentence"
      ></el-input>
      <el-button @click="addComment">提交评论</el-button>
    </div>
  </div>
</template>

<script>
import { reactive, onBeforeMount, ref } from "vue";
import { ElMessage } from "element-plus";
import { getComments } from "@/apis";

export default {
  name: "commentView",
  setup() {
    let commentsList = reactive({
      data: [],
    });

    let commentSentence = ref("");

    onBeforeMount(() => {
      flushCommentsList();
    });

    const flushCommentsList = () => {
      getComments({}).then((res) => {
        ElMessage({
          showClose: true,
          message: "一共有" + res.data.commentData.length + "条评论记录！",
          type: "success",
        });
        commentsList.data = res.data.commentData;
      });
    };

    const addComment = () => {
      if (commentSentence.value.length === 0) {
        ElMessage({
          showClose: true,
          message: "请输入评论内容！",
          type: "warning",
        });
      } else {
        ElMessage({
          showClose: true,
          message: "谢谢您为我们的系统留下评论！",
          type: "success",
        });
      }
      console.log(commentSentence.value);
    };

    return {
      commentsList,
      flushCommentsList,
      addComment,
      commentSentence,
    };
  },
};
</script>

<style scoped>
#comment-header {
  margin: auto 0;
}
</style>
