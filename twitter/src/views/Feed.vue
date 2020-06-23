<template>
    <div class="container">
      <div class="row">
        <div class="col">
          Feed component
        </div>
      </div>
      <div v-for="status in statuses" :key="status.id">
      <TweetCard :status="status"/>
      </div>
    </div>
</template>

<script>
import TweetCard from '../components/TweetCard.vue';

export default {
  components: {
    TweetCard,
  },
  data() {
    return {
      statuses: [
        {
          id: 'f5d597bc-259c-41fa-86df-73b7bea4c1e1',
          url: 'http://127.0.0.1:8000/api/tweets/f5d597bc-259c-41fa-86df-73b7bea4c1e1/',
          user: {
            id: 'ac2ed48a-e711-499d-abc2-4ac27330ed6c',
            url: 'http://127.0.0.1:8000/api/users/ac2ed48a-e711-499d-abc2-4ac27330ed6c/',
            screen_name: 'macieyn',
            name: 'Maciej Nachtygal',
            location: null,
            description: null,
            verified: false,
            profile_banner: null,
            profile_image: null,
            followers: [],
            following: [],
          },
          created_at: '2020-06-21T15:16:05Z',
          text: 'Hello Twitter!',
          favourited: [],
          reply_to: [],
          quoted_status: [],
          retweeted_status: [],
          entities: [],
        },
        {
          id: '1e284a5e-0810-43db-b2fd-617de4b73c78',
          url: 'http://127.0.0.1:8000/api/tweets/1e284a5e-0810-43db-b2fd-617de4b73c78/',
          user: {
            id: '30da6d56-466c-4486-ad2e-6e88a90f7a08',
            url: 'http://127.0.0.1:8000/api/users/30da6d56-466c-4486-ad2e-6e88a90f7a08/',
            screen_name: 'sillyboy',
            name: 'SillyBoy',
            location: null,
            description: null,
            verified: false,
            profile_banner: null,
            profile_image: null,
            followers: [],
            following: [],
          },
          created_at: '2020-06-21T15:44:56Z',
          text: 'Retweet!',
          favourited: [
            'ac2ed48a-e711-499d-abc2-4ac27330ed6c',
          ],
          reply_to: [],
          quoted_status: [],
          retweeted_status: [
            'f5d597bc-259c-41fa-86df-73b7bea4c1e1',
          ],
          entities: [],
        },
        {
          id: 'c5d6abde-d0f2-40f4-9bd1-011cba056a26',
          url: 'http://127.0.0.1:8000/api/tweets/c5d6abde-d0f2-40f4-9bd1-011cba056a26/',
          user: {
            id: '30da6d56-466c-4486-ad2e-6e88a90f7a08',
            url: 'http://127.0.0.1:8000/api/users/30da6d56-466c-4486-ad2e-6e88a90f7a08/',
            screen_name: 'sillyboy',
            name: 'SillyBoy',
            location: null,
            description: null,
            verified: false,
            profile_banner: null,
            profile_image: null,
            followers: [],
            following: [],
          },
          created_at: '2020-06-21T15:46:56Z',
          text: 'Reply to tweet',
          favourited: [
            'ac2ed48a-e711-499d-abc2-4ac27330ed6c',
          ],
          reply_to: [
            'f5d597bc-259c-41fa-86df-73b7bea4c1e1',
          ],
          quoted_status: [],
          retweeted_status: [],
          entities: [],
        },
        {
          id: '06af371b-92a9-46a6-a6cf-d0d14210105b',
          url: 'http://127.0.0.1:8000/api/tweets/06af371b-92a9-46a6-a6cf-d0d14210105b/',
          user: {
            id: '30da6d56-466c-4486-ad2e-6e88a90f7a08',
            url: 'http://127.0.0.1:8000/api/users/30da6d56-466c-4486-ad2e-6e88a90f7a08/',
            screen_name: 'sillyboy',
            name: 'SillyBoy',
            location: null,
            description: null,
            verified: false,
            profile_banner: null,
            profile_image: null,
            followers: [],
            following: [],
          },
          created_at: '2020-06-21T15:47:22Z',
          text: 'Quoted',
          favourited: [
            'ac2ed48a-e711-499d-abc2-4ac27330ed6c',
          ],
          reply_to: [],
          quoted_status: [
            {
              id: 'f5d597bc-259c-41fa-86df-73b7bea4c1e1',
              url: 'http://127.0.0.1:8000/api/tweets/f5d597bc-259c-41fa-86df-73b7bea4c1e1/',
              user: {
                id: 'ac2ed48a-e711-499d-abc2-4ac27330ed6c',
                url: 'http://127.0.0.1:8000/api/users/ac2ed48a-e711-499d-abc2-4ac27330ed6c/',
                screen_name: 'macieyn',
                name: 'Maciej Nachtygal',
                location: null,
                description: null,
                verified: false,
                profile_banner: null,
                profile_image: null,
                followers: [],
                following: [],
              },
              created_at: '2020-06-21T15:16:05Z',
              text: 'Hello Twitter!',
              favourited: [],
              reply_to: [],
              quoted_status: [],
              retweeted_status: [],
              entities: [],
            },
          ],
          retweeted_status: [],
          entities: [],
        },
      ],
    };
  },
};
</script>
<style lang="scss" scoped>
</style>
