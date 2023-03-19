{ pkgs }: {
    deps = [
        pkgs.python310Packages.pip
        pkgs.python310
        pkgs.htmltest
        pkgs.csslint
    ];
}