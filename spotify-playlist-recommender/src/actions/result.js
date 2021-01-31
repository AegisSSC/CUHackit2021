import {
  SET_ALBUMS,
  ADD_ALBUMS,
  SET_PLAYLIST,
  ADD_PLAYLIST
} from '../utils/constants';
import { get } from '../utils/api';

export const setAlbums = (albums) => ({
  type: SET_ALBUMS,
  albums
});

export const addAlbums = (albums) => ({
  type: ADD_ALBUMS,
  albums
});

export const setPlayList = (playlists) => ({
  type: SET_PLAYLIST,
  playlists
});

export const addPlaylist = (playlists) => ({
  type: ADD_PLAYLIST,
  playlists
});

export const initiateGetResult = (searchTerm) => {
  return async (dispatch) => {
    try {
      console.log(searchTerm);
      const API_URL = 'https://api.spotify.com/v1/users/spotify/playlist/' + searchTerm;
      // const API_URL = `https://api.spotify.com/v1/search?query=${encodeURIComponent(
      //   searchTerm
      // )}&type=playlists`;
      const result = await get(API_URL);
      console.log(result);
      const { albums, playlists } = result;
      dispatch(setAlbums(albums));
      return dispatch(setPlayList(playlists));
    } catch (error) {
      console.log('error', error);
    }
  };
};

// export const initiateLoadMoreAlbums = (url) => {
//   return async (dispatch) => {
//     try {
//       const result = await get(url);
//       return dispatch(addAlbums(result.albums));
//     } catch (error) {
//       console.log('error', error);
//     }
//   };
// };

// // export const initiateLoadMoreArtists = (url) => {
// //   return async (dispatch) => {
// //     try {
// //       const result = await get(url);
// //       return dispatch(addArtists(result.artists));
// //     } catch (error) {
// //       console.log('error', error);
// //     }
// //   };
// // };

// export const initiateLoadMorePlaylist = (url) => {
//   return async (dispatch) => {
//     try {
//       const result = await get(url);
//       return dispatch(addPlaylist(result.playlists));
//     } catch (error) {
//       console.log('error', error);
//     }
//   };
// };
