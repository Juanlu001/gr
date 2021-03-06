   UNAME_S := $(shell uname -s)

      GRDIR = /usr/local/gr
     LIBDIR = $(DESTDIR)$(GRDIR)/lib

     CFLAGS = -O -Wall -fPIC $(EXTRA_CFLAGS)
   CXXFLAGS = -O -Wall -fPIC $(EXTRA_CXXFLAGS)
   INCLUDES = -I.. -I../../../3rdparty
    SOFLAGS = -shared
    LDFLAGS = $(EXTRA_LDFLAGS)
  WX_CONFIG = false
     WXDEFS =
      WXINC = `$(WX_CONFIG) --cxxflags 2>/dev/null`
     WXLIBS = `$(WX_CONFIG) --libs 2>/dev/null`
ifeq ($(UNAME_S),Darwin)
ifneq ($(WXLIBS),)
     WXLIBS += -mmacosx-version-min=10.5
endif
endif
     QTDEFS =
      QTINC = -I$(QTDIR)/include
ifeq ($(UNAME_S),Darwin)
ifneq ($(QTINC),)
     QTINC += -mmacosx-version-min=10.5
endif
endif
     QTLIBS = -L$(QTDIR)/lib -lQtGui -lQtCore
 GTK_CONFIG = false
    GTKDEFS =
     GTKINC = `$(GTK_CONFIG) gtk+-2.0 --cflags 2>/dev/null`
    GTKLIBS = `$(GTK_CONFIG) gtk+-2.0 --libs 2>/dev/null`
   JPEGLIBS = ../../../3rdparty/jpeg/libjpeg.a
    PNGLIBS = ../../../3rdparty/libpng16/libpng.a
    BZ2LIBS = ../../../3rdparty/bzip2/libbz2.a
     GSDEFS = 
      GSINC =
     GSLIBS = -lgs
   GLFWDEFS =
    GLFWINC =
    GLFWLIB = glfw
ifeq ($(UNAME_S),Darwin)
   GLFWLIBS = -l$(GLFWLIB) -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo
else
   GLFWLIBS = -l$(GLFWLIB) -lGL
endif
    XFTDEFS =
     FTDEFS =
      FTINC = -I../../../3rdparty/freetype/include
     FTLIBS = ../../../3rdparty/freetype/libfreetype.a
     AVDEFS = 
     AVLIBS = -lavdevice -lavformat -lavfilter -lavcodec -lswscale -lavutil -ltheora -logg -lvpx
  MUPDFDEFS = 
  MUPDFLIBS = -lmupdf $(FTLIBS) -ljbig2dec $(JPEGLIBS) -lopenjp2 $(BZ2LIBS)
    SSLLIBS = -lssl -lcrypto
    X11DEFS =
    XFTLIBS = -lXft -lfontconfig
    X11LIBS = $(X11PATH) $(XFTLIBS) -lXt -lX11
    ZMQDEFS = 
    ZMQLIBS = -lzmq -lpthread
  EXTRALIBS =
       LIBS = -lc -lm
       ZINC = -I../../../3rdparty/zlib
      ZLIBS = ../../../3rdparty/zlib/libz.a

.SUFFIXES: .o .m .cxx

.m.o:
	$(CXX) -c -DGRDIR=\"$(GRDIR)\" $(DEFINES) $(INCLUDES) $(CXXFLAGS) $<
.c.o:
	$(CC) -c -DGRDIR=\"$(GRDIR)\" $(AVDEFS) $(MUPDFDEFS) $(CFLAGS) $<
.cxx.o:
	$(CXX) -c -DGRDIR=\"$(GRDIR)\" $(DEFINES) $(WXDEFS) $(WXINC) $(QTDEFS) $(QTINC) $(GTKDEFS) $(GTKINC) $(GSDEFS) $(GSINC) $(GLFWDEFS) $(GLFWINC) $(ZMQDEFS) $(INCLUDES) $(XFTDEFS) $(FTDEFS) $(FTINC) $(AVDEFS) $(MUPDFDEFS) $(X11DEFS) $(X11INC) $(CXXFLAGS) $(ZINC) $<

default:
	@make -C ../../.. Makedefs
	@make `cat ../../../Makedefs`

targets: prerequisites \
         wxplugin.so qtplugin.so svgplugin.so gtkplugin.so figplugin.so \
         gsplugin.so wmfplugin.so glplugin.so zmqplugin.so movplugin.so \
         htmplugin.so pgfplugin.so

prerequisites:
	@for d in libpng16; do make -C ../../../3rdparty/$$d; done

Darwin:
	@make targets quartzplugin.so \
	EXTRALIBS="-framework VideoDecodeAcceleration -framework CoreVideo -framework CoreFoundation" LIBS="-liconv"
Linux:
	@make targets \
	SOFLAGS="-shared" LDFLAGS="$(EXTRA_LDFLAGS) -Wl,-rpath=$(QTDIR)/lib"

wxplugin.so: wxplugin.o font.o afm.o util.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(WXLIBS) $(LDFLAGS) $(X11LIBS) $(LIBS)

qtplugin.so: qtplugin.o font.o afm.o util.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(QTLIBS) $(LDFLAGS) $(X11LIBS) $(LIBS)

svgplugin.so: svgplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(PNGLIBS) $(ZLIBS) $(LIBS)

gtkplugin.so: gtkplugin.o font.o afm.o util.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(GTKLIBS) $(LDFLAGS) $(X11LIBS) $(LIBS)

figplugin.so: figplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(PNGLIBS) $(ZLIBS) $(LIBS)

gsplugin.so: gsplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LDFLAGS) $(GSLIBS) $(X11LIBS) $(LIBS)

wmfplugin.so: wmfplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LDFLAGS) $(LIBS)

quartzplugin.so: quartzplugin.o font.o afm.o util.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LIBS) \
	-lobjc -framework Foundation -framework ApplicationServices -framework AppKit

glplugin.so: glplugin.o font.o afm.o util.o ft.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LDFLAGS) $(GLFWLIBS) $(FTLIBS) $(X11LIBS) $(LIBS)

zmqplugin.so: zmqplugin.o font.o afm.o util.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LDFLAGS) $(ZMQLIBS) $(LIBS)

movplugin.so: movplugin.o font.o afm.o util.o vc.o gif.o dl.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(LDFLAGS) $(AVLIBS) $(MUPDFLIBS) $(SSLLIBS) $(EXTRALIBS) $(ZLIBS) $(LIBS)

htmplugin.so: htmplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(PNGLIBS) $(ZLIBS) $(LIBS)

pgfplugin.so: pgfplugin.o font.o afm.o util.o malloc.o error.o io.o
	$(CXX) -o $@ $(SOFLAGS) $? $(PNGLIBS) $(ZLIBS) $(LIBS)

install: default $(TARGETS)
	cp -p *.so $(LIBDIR)

clean:
	rm -f so_locations *.so *.o *.bak *~ *.tmp
