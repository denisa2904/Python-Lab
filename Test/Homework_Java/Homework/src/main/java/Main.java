
import entity.Album;
import entity.Artist;
import entity.Genre;
import entity.Playlist;
import repository.AlbumRepo;
import repository.ArtistRepo;
import repository.GenreRepo;
import repository.PlaylistRepo;

import java.util.List;
import java.util.Optional;

public class Main {
    public static void main(String[] args) {
        ArtistRepo artistRepo = new ArtistRepo();
        GenreRepo genreRepo = new GenreRepo();
        AlbumRepo albumRepo = new AlbumRepo();
        PlaylistRepo playlistRepo = new PlaylistRepo();

        /*for(int i = 0; i < 100; i++) {
            String name = "artist" + i;
            Artist artist = new Artist(name);
            artistRepo.create(artist);
        }*/
        System.out.println(artistRepo.findAll() + "\n");
        System.out.println(artistRepo.findByName("Doja Cat").orElseThrow(() -> new RuntimeException("Artist not found")) + "\n");

        System.out.println(genreRepo.findAll() + "\n");

        /*for(int i = 1; i < 100; i++) {
            String name = "album" + i;
            Album album = new Album(1950 + i, name, artistRepo.findById(i).orElseThrow(() -> new RuntimeException("Artist not found")), List.of(genreRepo.findById(1).orElseThrow(() -> new RuntimeException("Genre not found"))));
            albumRepo.create(album);
        }*/

        /* Create an album */
        Optional<Artist> artistMaybe = artistRepo.findById(2);
        Artist artist = artistMaybe.orElseThrow(() -> new RuntimeException("Artist not found"));
        Genre genre = genreRepo.findByName("Pop").orElseThrow(() -> new RuntimeException("Genre not found"));
        Album album = new Album(1999, "Christina ", artist, List.of(genre));
        albumRepo.create(album);

        System.out.println(albumRepo.findAll() + "\n");

        /* Create  a playlist */
        /*Album album1 = albumRepo.findByName("Planet Her").orElseThrow(() -> new RuntimeException("Album not found"));
        Playlist playlist = new Playlist("Playlist2", List.of(album));
        playlistRepo.create(playlist);*/
        System.out.println(playlistRepo.findAll() + "\n");
    }
}
