FROM sagemath/sagemath:latest

USER root

COPY downloads/ctbllib-1.3.11.tar.gz  /tmp/ctbllib.tar.gz
COPY downloads/utils-0.96.tar.gz      /tmp/utils.tar.gz
COPY downloads/atlasrep-2.1.11.tar.gz /tmp/atlasrep.tar.gz

RUN PKG=/home/sage/sage/local/lib/gap/pkg && \
    rm -rf $PKG/ctbllib && \
    tar -xzf /tmp/ctbllib.tar.gz  -C $PKG && mv $PKG/ctbllib-1.3.11  $PKG/ctbllib && \
    tar -xzf /tmp/utils.tar.gz    -C $PKG && \
    tar -xzf /tmp/atlasrep.tar.gz -C $PKG && \
    rm /tmp/ctbllib.tar.gz /tmp/utils.tar.gz /tmp/atlasrep.tar.gz

USER sage
WORKDIR /home/sage/work
COPY . .
