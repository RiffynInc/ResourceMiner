library(rmongodb)

m <- mongo.create(host="ec2-52-26-49-156.us-west-2.compute.amazonaws.com", 
                  username="mozsprint", password="plos", db="plos")

colls <- c('plos_biol',
         'plos_genet',
         'plos_med',
         'plos_negl_trop_dis',
         'plos_one',
         'plos_pathog')

