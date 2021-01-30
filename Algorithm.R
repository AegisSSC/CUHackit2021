library('httr')
library('jsonlite')
library('dplyr')
library('tidyr')
library('zoo')
library('purrr')
library('RCurl')


if(!file.exists(".spotify")){
  print("no file")
  
  #to get token FIRST TIME
  browseURL(paste0('https://accounts.spotify.com/authorize?client_id=',client_id,'&response_type=code&redirect_uri=',website_uri,'/&scope=user-read-recently-played'),browser = getOption("browser"), encodeIfNeeded = FALSE)
  
  #add new token
  user_code <- user_code_value
  
  #construct body of POST request FIRST TIME
  request_body <- list(grant_type='authorization_code',
                       code=user_code,
                       redirect_uri=website_uri, #input your domain name
                       client_id = sp_client_id, #input your Spotify Client ID
                       client_secret = sp_client_secret) #input your Spotify Client Secret
  
  #get user tokens FIRST TIME
  user_token <- httr::content(httr::POST('https://accounts.spotify.com/api/token',
                                         body=request_body,
                                         encode='form'))
  
  user_token$access_token -> token
  auth_header <- httr::add_headers('Authorization'= paste('Bearer',token))
  write(user_token$refresh_token, ".spotify")
  
}

if(file.exists(".spotify")) {
  print("we have file")
  
  #REFRESH
  scan(file = ".spotify", what= list(id="")) -> red
  as.character(red) -> refresh_code
  request_body_refresh <- list(grant_type='refresh_token',
                               refresh_token=refresh_code,
                               redirect_uri=website_uri,
                               client_id = sp_client_id,
                               client_secret = sp_client_secret)
  
  #get user tokens REFRESH
  user_token_refresh <- httr::content(httr::POST('https://accounts.spotify.com/api/token',
                                                 body=request_body_refresh,
                                                 encode='form'))
  user_token_refresh$access_token -> token
}