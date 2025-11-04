"""Unit tests for config.py"""

from pathlib import Path

from codemapper.config import get_output_directory, load_user_config


def test_load_user_config_no_file(temp_dir, monkeypatch):
    """Test loading config when no config file exists."""
    monkeypatch.setattr(Path, "home", lambda: temp_dir)
    config = load_user_config()
    assert config == {}


def test_load_user_config_exists(temp_dir, monkeypatch):
    """Test loading config from ~/.codemapper/codemapper.toml."""
    monkeypatch.setattr(Path, "home", lambda: temp_dir)

    config_dir = temp_dir / ".codemapper"
    config_dir.mkdir()
    config_file = config_dir / "codemapper.toml"
    config_file.write_text('output_dir = "/tmp/codemaps"\nprefix_style = "underscore"\n', encoding="utf-8")

    config = load_user_config()
    assert config["output_dir"] == "/tmp/codemaps"
    assert config["prefix_style"] == "underscore"


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
    assert "~" not in output_dir
    assert output_dir.startswith("/")


def test_get_output_directory_precedence():
    """Test precedence: CLI > output_dir > prefix_style > default."""
    # With all options, CLI should win
    config = {"output_dir": "/config/dir", "prefix_style": "underscore"}
    assert get_output_directory(cli_output_dir="/cli/dir", config=config) == "/cli/dir"

    # With config, output_dir should beat prefix_style
    config = {"output_dir": "/config/dir", "prefix_style": "underscore"}
    assert get_output_directory(config=config) == "/config/dir"

    # With just prefix_style
    config = {"prefix_style": "underscore"}
    assert get_output_directory(config=config) == "./_codemaps"
