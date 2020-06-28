<template>
  <div>
    <div class="wrapper">
      <div class="profile-image">
        <div v-if="status.user.profile_image">
          <img :src="status.user.profile_image" class="circle-border"/>
        </div>
        <div v-else>
          <div class="circle-border initials">
            {{ userInitials }}
          </div>
          <div v-if="reply" class="line-container">
            <div class="line">
            </div>
          </div>
        </div>
      </div>
      <div class="content">
        <div class="info">
          <TweetInfo :status="status" />
        </div>
        <div class="content">
          {{ status.text }}
          <Quote v-if="status.quoted_status" :status="status.quoted_status" />
        </div>
        <TweetActionBar :status="status" />
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import Quote from './Quote.vue';
import TweetActionBar from './TweetActionBar.vue';
import TweetInfo from './TweetInfo.vue';

export default {
  name: 'Tweet',
  components: {
    Quote,
    TweetActionBar,
    TweetInfo,
  },
  props: {
    status: {
      type: Object,
      required: true,
    },
    reply: {
      type: Boolean,
      required: false,
    },
  },
  methods: {
  },
  computed: {
    timeDiff() {
      const createdAt = moment(this.status.created_at);
      if (createdAt.isAfter(moment().subtract(1, 'days'))) return createdAt.fromNow(true);
      if (createdAt.isAfter(moment().startOf('year'))) return createdAt.format('DD MMM');
      return createdAt.format('DD MMM, YYYY');
    },
    userInitials() {
      return this.status.user.name.match(/\b(\w)/g).join('');
    },
  },
  mounted() {
  },
};
</script>

<style lang="scss" scoped>
.circle-border {
  border-radius: 50%;
  width: 50px;
  height: 50px;
  min-width: 50px;
  min-height: 50px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 20px;
  background-color: rgb(85, 168, 250);
}
.wrapper {
  display: flex;
  flex-direction: row;
  // border: 1px solid lightgrey;
  padding: 15px;
  padding-bottom: 5px;
  border-radius: 15px;
  background-color: #fff;
  box-shadow: 0px 2px 2px 0px rgba(200,200,200,0.5);
  margin: 5px 0 10px 0;
}
.profile-image {
  margin: 0 15px 0 0;
}
.info {
  display: flex;
  flex-direction: row;
}
.content {
  width: 100%;
  margin-top: 5px;
}
.line {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 1px solid lightskyblue;
  width: 0;
  margin: 5px 0;
  flex: 1;
}
.line-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
  min-height: 100%;
}
</style>
