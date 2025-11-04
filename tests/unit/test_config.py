"""Unit tests for config.py"""

from pathlib import Path

from codemapper.config import get_output_directory, load_user_config


def test_load_user_config_no_file(temp_dir, monkeypatch):
    """Test loading config when no config file exists."""
    # Mock Path.home() to use temp_dir
    monkeypatch.setattr(Path, "home", lambda: temp_dir)

    config = load_user_config()
    assert config == {}


def test_load_user_config_xdg_location(temp_dir, monkeypatch):
    """Test loading config from ~/.config/codemapper/config.toml."""
    monkeypatch.setattr(Path, "home", lambda: temp_dir)

    config_dir = temp_dir / ".config" / "codemapper"
    config_dir.mkdir(parents=True)
    config_file = config_dir / "config.toml"
    config_file.write_text('output_dir = "/tmp/codemaps"\nprefix_style = "underscore"\n', encoding="utf-8")

    config = load_user_config()
    assert config["output_dir"] == "/tmp/codemaps"
    assert config["prefix_style"] == "underscore"


def test_load_user_config_home_location(temp_dir, monkeypatch):
    """Test loading config from ~/.codemapper.toml."""
    monkeypatch.setattr(Path, "home", lambda: temp_dir)

    config_file = temp_dir / ".codemapper.toml"
    config_file.write_text('output_dir = "/home/codemaps"\n', encoding="utf-8")

    config = load_user_config()
    assert config["output_dir"] == "/home/codemaps"


def test_load_user_config_precedence(temp_dir, monkeypatch):
    """Test that XDG location takes precedence over home location."""
    monkeypatch.setattr(Path, "home", lambda: temp_dir)

    # Create config in both locations
    config_dir = temp_dir / ".config" / "codemapper"
    config_dir.mkdir(parents=True)
    (config_dir / "config.toml").write_text('output_dir = "/xdg/path"\n', encoding="utf-8")
    (temp_dir / ".codemapper.toml").write_text('output_dir = "/home/path"\n', encoding="utf-8")

    config = load_user_config()
    # XDG should win
    assert config["output_dir"] == "/xdg/path"


def test_get_output_directory_default():
    """Test default output directory."""
    output_dir = get_output_directory()
    assert output_dir == "./.codemaps"


def test_get_output_directory_cli_override():
    """Test that CLI flag takes highest precedence."""
    config = {"output_dir": "/config/path", "prefix_style": "underscore"}
    output_dir = get_output_directory(cli_output_dir="/cli/path", config=config)
    assert output_dir == "/cli/path"


def test_get_output_directory_from_config():
    """Test using output_dir from config."""
    config = {"output_dir": "/config/path"}
    output_dir = get_output_directory(config=config)
    assert output_dir == "/config/path"


def test_get_output_directory_prefix_style_dot():
    """Test prefix_style=dot."""
    config = {"prefix_style": "dot"}
    output_dir = get_output_directory(config=config)
    assert output_dir == "./.codemaps"


def test_get_output_directory_prefix_style_underscore():
    """Test prefix_style=underscore."""
    config = {"prefix_style": "underscore"}
    output_dir = get_output_directory(config=config)
    assert output_dir == "./_codemaps"


def test_get_output_directory_prefix_style_dash():
    """Test prefix_style=dash."""
    config = {"prefix_style": "dash"}
    output_dir = get_output_directory(config=config)
    assert output_dir == "./-codemaps"


def test_get_output_directory_prefix_style_invalid():
    """Test invalid prefix_style falls back to dot."""
    config = {"prefix_style": "invalid"}
    output_dir = get_output_directory(config=config)
    assert output_dir == "./.codemaps"


def test_get_output_directory_expands_tilde():
    """Test that ~ is expanded in paths."""
    output_dir = get_output_directory(cli_output_dir="~/my-codemaps")
    assert output_dir.startswith("/")
    assert "~" not in output_dir
