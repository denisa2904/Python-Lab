PGDMP     7                     {           lab9    15.2    15.2 %    +           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ,           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            -           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            .           1262    22910    lab9    DATABASE        CREATE DATABASE lab9 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE lab9;
                postgres    false            �            1259    22932    albums    TABLE     �   CREATE TABLE public.albums (
    id integer NOT NULL,
    release_year integer NOT NULL,
    name character varying NOT NULL,
    artist_id integer NOT NULL
);
    DROP TABLE public.albums;
       public         heap    postgres    false            �            1259    23053    albums_genres_associations    TABLE     q   CREATE TABLE public.albums_genres_associations (
    album_id integer NOT NULL,
    genre_id integer NOT NULL
);
 .   DROP TABLE public.albums_genres_associations;
       public         heap    postgres    false            �            1259    22931    albums_id_seq    SEQUENCE     �   ALTER TABLE public.albums ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.albums_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            �            1259    22912    artists    TABLE     ^   CREATE TABLE public.artists (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.artists;
       public         heap    postgres    false            �            1259    22911    artists_id_seq    SEQUENCE     �   ALTER TABLE public.artists ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.artists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            �            1259    22922    genres    TABLE     ]   CREATE TABLE public.genres (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.genres;
       public         heap    postgres    false            �            1259    22921    genres_id_seq    SEQUENCE     �   ALTER TABLE public.genres ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.genres_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            �            1259    23067    playlist    TABLE     }   CREATE TABLE public.playlist (
    id integer NOT NULL,
    created_at date NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.playlist;
       public         heap    postgres    false            �            1259    23066    playlist_id_seq    SEQUENCE     �   ALTER TABLE public.playlist ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.playlist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    222            �            1259    23072    playlists_albums_associations    TABLE     w   CREATE TABLE public.playlists_albums_associations (
    playlist_id integer NOT NULL,
    album_id integer NOT NULL
);
 1   DROP TABLE public.playlists_albums_associations;
       public         heap    postgres    false            $          0    22932    albums 
   TABLE DATA           C   COPY public.albums (id, release_year, name, artist_id) FROM stdin;
    public          postgres    false    219   �(       %          0    23053    albums_genres_associations 
   TABLE DATA           H   COPY public.albums_genres_associations (album_id, genre_id) FROM stdin;
    public          postgres    false    220   	)                  0    22912    artists 
   TABLE DATA           +   COPY public.artists (id, name) FROM stdin;
    public          postgres    false    215   *)       "          0    22922    genres 
   TABLE DATA           *   COPY public.genres (id, name) FROM stdin;
    public          postgres    false    217   \)       '          0    23067    playlist 
   TABLE DATA           8   COPY public.playlist (id, created_at, name) FROM stdin;
    public          postgres    false    222   )       (          0    23072    playlists_albums_associations 
   TABLE DATA           N   COPY public.playlists_albums_associations (playlist_id, album_id) FROM stdin;
    public          postgres    false    223   �)       /           0    0    albums_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.albums_id_seq', 2, true);
          public          postgres    false    218            0           0    0    artists_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.artists_id_seq', 3, true);
          public          postgres    false    214            1           0    0    genres_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.genres_id_seq', 1, true);
          public          postgres    false    216            2           0    0    playlist_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.playlist_id_seq', 2, true);
          public          postgres    false    221            �           2606    22938    albums albums_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.albums DROP CONSTRAINT albums_pkey;
       public            postgres    false    219            �           2606    22940    albums albums_unique_name 
   CONSTRAINT     T   ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_unique_name UNIQUE (name);
 C   ALTER TABLE ONLY public.albums DROP CONSTRAINT albums_unique_name;
       public            postgres    false    219            }           2606    22918    artists artists_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.artists DROP CONSTRAINT artists_pkey;
       public            postgres    false    215                       2606    22920    artists artists_unique_name 
   CONSTRAINT     V   ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_unique_name UNIQUE (name);
 E   ALTER TABLE ONLY public.artists DROP CONSTRAINT artists_unique_name;
       public            postgres    false    215            �           2606    22928    genres genres_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.genres DROP CONSTRAINT genres_pkey;
       public            postgres    false    217            �           2606    22930    genres genres_unique_name 
   CONSTRAINT     T   ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_unique_name UNIQUE (name);
 C   ALTER TABLE ONLY public.genres DROP CONSTRAINT genres_unique_name;
       public            postgres    false    217            �           2606    23071    playlist playlist_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.playlist DROP CONSTRAINT playlist_pkey;
       public            postgres    false    222            �           2606    23088    playlist playlist_unique_name 
   CONSTRAINT     X   ALTER TABLE ONLY public.playlist
    ADD CONSTRAINT playlist_unique_name UNIQUE (name);
 G   ALTER TABLE ONLY public.playlist DROP CONSTRAINT playlist_unique_name;
       public            postgres    false    222            �           2606    23056 $   albums_genres_associations album_ref    FK CONSTRAINT     �   ALTER TABLE ONLY public.albums_genres_associations
    ADD CONSTRAINT album_ref FOREIGN KEY (album_id) REFERENCES public.albums(id);
 N   ALTER TABLE ONLY public.albums_genres_associations DROP CONSTRAINT album_ref;
       public          postgres    false    220    3205    219            �           2606    23080 *   playlists_albums_associations album_ref_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.playlists_albums_associations
    ADD CONSTRAINT album_ref_id FOREIGN KEY (album_id) REFERENCES public.albums(id);
 T   ALTER TABLE ONLY public.playlists_albums_associations DROP CONSTRAINT album_ref_id;
       public          postgres    false    219    3205    223            �           2606    23048    albums artist_ref    FK CONSTRAINT     ~   ALTER TABLE ONLY public.albums
    ADD CONSTRAINT artist_ref FOREIGN KEY (artist_id) REFERENCES public.artists(id) NOT VALID;
 ;   ALTER TABLE ONLY public.albums DROP CONSTRAINT artist_ref;
       public          postgres    false    219    215    3197            �           2606    23061 $   albums_genres_associations genre_ref    FK CONSTRAINT     �   ALTER TABLE ONLY public.albums_genres_associations
    ADD CONSTRAINT genre_ref FOREIGN KEY (genre_id) REFERENCES public.genres(id);
 N   ALTER TABLE ONLY public.albums_genres_associations DROP CONSTRAINT genre_ref;
       public          postgres    false    217    3201    220            �           2606    23075 *   playlists_albums_associations playlist_ref    FK CONSTRAINT     �   ALTER TABLE ONLY public.playlists_albums_associations
    ADD CONSTRAINT playlist_ref FOREIGN KEY (playlist_id) REFERENCES public.playlist(id);
 T   ALTER TABLE ONLY public.playlists_albums_associations DROP CONSTRAINT playlist_ref;
       public          postgres    false    3209    223    222            $      x�3�4202�t�I*�5�4����� 0      %      x�3�4����� f          "   x�3��M,I��2�t���2�I�I�\1z\\\ p�      "      x�3��/������ �      '   $   x�3�4202�50�50��I���,.1����� ZLf      (      x�3�4����� m      