import enum
from sqlalchemy import (
    create_engine, Column, Integer, String, Text, DateTime,
    Enum, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# ENUM for download status
class DownloadStatus(enum.Enum):
    pending = "pending"
    success = "success"
    failed = "failed"

class Platform(Base):
    __tablename__ = 'platforms'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    songs = relationship('Song', back_populates='platform')
    playlists = relationship('Playlist', back_populates='source_platform')
    linked_services = relationship('LinkedService', back_populates='platform')


class Download(Base):
    __tablename__ = 'downloads'

    id = Column(Integer, primary_key=True)
    status = Column(Enum(DownloadStatus), nullable=False)
    last_attempted = Column(DateTime)
    downloaded_at = Column(DateTime)
    error_message = Column(Text)
    source_url = Column(Text)
    file_type = Column(Text)  # e.g., 'mp3', 'flac'
    quality = Column(Text)    # e.g., '320kbps', 'lossless'

    songs = relationship('Song', back_populates='download')


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    album = Column(Text)
    year = Column(Integer)
    genre = Column(Text)
    file_id = Column(Text)
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    download_id = Column(Integer, ForeignKey('downloads.id'))

    platform = relationship('Platform', back_populates='songs')
    download = relationship('Download', back_populates='songs')
    artists = relationship('SongArtist', back_populates='song')
    playlist_links = relationship('PlaylistSong', back_populates='song')


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    songs = relationship('SongArtist', back_populates='artist')


class SongArtist(Base):
    __tablename__ = 'song_artists'

    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)
    artist_id = Column(Integer, ForeignKey('artists.id'), primary_key=True)

    song = relationship('Song', back_populates='artists')
    artist = relationship('Artist', back_populates='songs')


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    creator = Column(Text)
    location = Column(Text)
    source_platform = Column(Integer, ForeignKey('platforms.id'))
    cover = Column(Text)

    source_platform_rel = relationship('Platform', back_populates='playlists')
    songs = relationship('PlaylistSong', back_populates='playlist')


class PlaylistSong(Base):
    __tablename__ = 'playlist_songs'

    playlist_id = Column(Integer, ForeignKey('playlists.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)
    track_order = Column(Integer)

    playlist = relationship('Playlist', back_populates='songs')
    song = relationship('Song', back_populates='playlist_links')


class LinkedService(Base):
    __tablename__ = 'linked_services'

    id = Column(Integer, primary_key=True)
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    access_token = Column(Text)
    refresh_token = Column(Text)
    token_expiry = Column(DateTime)
    user_id = Column(Text)
    display_name = Column(Text)
    connected_at = Column(DateTime)

    platform = relationship('Platform', back_populates='linked_services')
