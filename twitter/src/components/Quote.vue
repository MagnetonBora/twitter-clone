<template>
  <div>
    <div class="wrapper">
      <div class="info">
        <div v-if="status.user.profile_image">
          <img :src="status.user.profile_image" class="circle-border"/>
        </div>
        <div v-else class="">
          <div class="circle-border initials">
            {{ userInitials }}
          </div>
        </div>
        <div>
          <TweetInfo :status="status" />
        </div>
      </div>
      <div class="content">
        {{ status.text }}
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';
import TweetInfo from './TweetInfo.vue';

export default {
  name: 'Quote',
  components: {
    TweetInfo,
  },
  props: {
    status: {
      type: Object,
      required: true,
    },
  },
  computed: {
    timeDiff() {
      const createdAt = new Date(this.status.created_at);
      const diff = new Date() - createdAt;
      if (diff < 86400000) return moment(createdAt).fromNow();
      return moment(createdAt).format('DD MMM');
    },
    userInitials() {
      return this.status.user.name.match(/\b(\w)/g).join('');
    },
  },
};
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  border: 1px solid lightgrey;
  margin: 10px 0;
  padding: 10px;
  border-radius: 15px;
  margin-right: 15px;
}
.circle-border {
  border-radius: 50%;
  width: 20px;
  height: 20px;
  min-width: 20px;
  min-height: 20px;
  margin-right: 5px;
}
.initials {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 10px;
  background-color: rgb(85, 168, 250);
}
.info {
  display: flex;
  flex-direction: row;
}
.content {
  margin-top: 5px;
}
</style>
