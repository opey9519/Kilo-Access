// AuthContext.tsx
import { createContext, useState, useEffect } from "react";
import type { ReactNode } from "react";
import { getToken, getRefreshToken } from "./api/utility/utility";
import { refreshAccessToken } from "./api/auth";
import { jwtDecode } from "jwt-decode";

interface UserState {
  isAuthenticated: boolean;
  token: string | null;
}

interface AuthContextType {
  user: UserState;
  loading: boolean;
  login: (access_token: string, refresh_token: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | null>(null);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<UserState>({
    isAuthenticated: false,
    token: null,
  });

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = getToken();
    const refresh_token = getRefreshToken();

    if (token && token !== "undefined") {
      try {
        const decoded: any = jwtDecode(token);
        const current_time = Date.now() / 1000;

        if (decoded.exp - current_time < 300) {
          refreshAccessToken(refresh_token ?? "");
        }
        setUser({ isAuthenticated: true, token });
      } catch {
        setUser({ isAuthenticated: false, token: null });
      }
    } else {
      setUser({ isAuthenticated: false, token: null });
    }
    setLoading(false);
  }, []);

  const login = (access_token: string, refresh_token: string) => {
    console.log(access_token)
    console.log(refresh_token)
    localStorage.setItem("token", access_token);
    localStorage.setItem("refresh_token", refresh_token);
    setUser({ isAuthenticated: true, token: access_token });
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
    setUser({ isAuthenticated: false, token: null });
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
