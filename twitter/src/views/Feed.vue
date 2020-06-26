<template>
    <div class="container">
      <div class="row">
        <div class="col">
          <!-- Feed component -->
        </div>
      </div>
      <div v-for="status in statuses" :key="status.id" class="my-5">
        <div v-if="status.retweeted_status.length === 1">
          <Retweet :status="status"/>
        </div>
        <div v-else-if="status.reply_to.length === 1">
          <Reply :status="status"/>
        </div>
        <div v-else>
          <Tweet :status="status"/>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import Reply from '../components/Reply.vue';
import Retweet from '../components/Retweet.vue';
import Tweet from '../components/Tweet.vue';

export default {
  components: {
    Reply,
    Retweet,
    Tweet,
  },
  data() {
    return {
      statuses: [],
    };
  },
  methods: {
    getStatuses() {
      axios.get('http://127.0.0.1:8000/api/tweets/')
        .then((response) => {
          console.log(response);
          this.statuses = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.getStatuses();
  },
};
</script>
<style lang="scss" scoped>
* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
