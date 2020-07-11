<template>
  <div class="wrapper">
    <div v-if="$store.state.isAuthenticated">
      <TweetInput @add-status="addStatus"/>
    </div>
    <div v-for="status in statuses" :key="status.id">
      <div v-if="status.retweeted_status">
        <Retweet :status="status" class="border"/>
      </div>
      <div v-else-if="status.reply_to">
        <Reply :status="status" class="border"/>
      </div>
      <div v-else>
        <Tweet :status="status" class="border"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Reply from '../components/Reply.vue';
import Retweet from '../components/Retweet.vue';
import Tweet from '../components/Tweet.vue';
import TweetInput from '../components/TweetInput.vue';

export default {
  name: 'Feed',
  components: {
    Reply,
    Retweet,
    Tweet,
    TweetInput,
  },
  data() {
    return {
      statuses: [],
    };
  },
  methods: {
    getStatuses() {
      axios.get(
        'http://127.0.0.1:8000/api/tweets/',
        { headers: { Authorization: `Bearer ${this.$store.state.jwt}` } },
      )
        .then((response) => {
          console.log(response);
          this.statuses = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addStatus(status) {
      axios.get(
        `http://127.0.0.1:8000/api/tweets/${status.id}`,
        { headers: { Authorization: `Bearer ${this.$store.state.jwt}` } },
      )
        .then((response) => {
          console.log(response);
          this.statuses = [response.data, ...this.statuses];
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
// * {
//   box-sizing: border-box;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
// }
.wrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 600px;
}
.border {
  // outline: 1px solid lightgrey;
  padding: 5px 0;
}
</style>
